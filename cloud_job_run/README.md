# Cloud Job Run

## Request

```sh
curl --location 'https://run.googleapis.com/v2/projects/[PROJECT]/locations/us-central1/jobs/run-demo-job:run' \
--header 'Authorization: Bearer [TOKEN]' \
--header 'Content-Type: application/json' \
--data '{
    "overrides": {
        "containerOverrides": [
            {
                "args": [
                    "python",
                    "src/main.py",
                    "arg1",
                    "arg2"
                ],
                "env": [
                    {
                        "name": "VAR1",
                        "value": "x"
                    },
                    {
                        "name": "VAR2",
                        "value": "y"
                    }
                ]
            }
        ]
    }
}'

```

## References

- https://cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs
- https://cloud.google.com/run/docs/reference/rest/v1/namespaces.jobs/run
