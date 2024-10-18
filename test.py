import subprocess


def test_extract():
    """Test extractData()"""
    result = subprocess.run(
        ["python3", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert (
        result.returncode == 0
    ), f"Extract failed with return code {result.returncode}"
    assert (
        "Extracting data..." in result.stdout
    ), "Expected 'Extracting data...' in output"
    print("Extract Test Passed!")


def test_load():
    """Test loadData()"""
    result = subprocess.run(
        ["python3", "main.py", "load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0, f"Load failed with return code {result.returncode}"
    assert (
        "Loading data to Databricks..." in result.stdout
    ), "Expected 'Loading data to Databricks...' in output"
    print("Load Test Passed!")


def test_query():
    """Test queryData() with a complex SQL query"""
    query_string = """
        WITH all_matches AS (
            SELECT '2019' AS season, Team1 AS team, Team2 AS opponent, 
                CAST(SPLIT_PART(FT, '-', 1) AS INT) AS goals_scored,
                CAST(SPLIT_PART(FT, '-', 2) AS INT) AS goals_conceded
            FROM MatchResults2019DB
            UNION ALL
            SELECT 'previous' AS season, Team1 AS team, Team2 AS opponent, 
                CAST(SPLIT_PART(FT, '-', 1) AS INT) AS goals_scored,
                CAST(SPLIT_PART(FT, '-', 2) AS INT) AS goals_conceded
            FROM MatchResultsDB
        ),
        team_matches AS (
            SELECT team, opponent, 
                AVG(goals_scored) AS avg_goals_scored, 
                COUNT(*) AS total_matches_played
            FROM all_matches
            WHERE team IN (
                SELECT DISTINCT team FROM (
                    SELECT Team1 AS team FROM MatchResults2019DB
                    UNION ALL
                    SELECT Team2 AS team FROM MatchResults2019DB
                    INTERSECT
                    SELECT Team1 AS team FROM MatchResultsDB
                    UNION ALL
                    SELECT Team2 AS team FROM MatchResultsDB
                ) AS common_teams
            )
            GROUP BY team, opponent
        )

        SELECT team, opponent, avg_goals_scored, total_matches_played
        FROM team_matches
        ORDER BY total_matches_played DESC
        LIMIT 10;
    """

    result = subprocess.run(
        ["python3", "main.py", "query", query_string],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0, f"Query failed with return code {result.returncode}"
    assert "team" in result.stdout, "Expected 'team' in the query result"
    assert "opponent" in result.stdout, "Expected 'opponent' in the query result"
    print("Query Test Passed!")


if __name__ == "__main__":
    test_extract()
    test_load()
    test_query()
