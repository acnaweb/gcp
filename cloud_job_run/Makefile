export LOCAL_IMAGE=us-central1-docker.pkg.dev/dd8-data-hml/efemeral/image

c_build:
	docker build -t ${LOCAL_IMAGE} .

c_run:
	docker run --rm ${LOCAL_IMAGE} "Carlos" "30"

c_push:
	docker push ${LOCAL_IMAGE}

deploy:
	gcloud run jobs create run-demo-job \
    --image=${LOCAL_IMAGE} \
    --region=us-central1 \
    --task-timeout=300s \
    --max-retries=1

run_job:
	gcloud run jobs execute run-demo-job --region=us-central1 --args '{"nome": "Carlos", "idade": 30}'

request1:	
	curl -X POST https://run.googleapis.com/v2/projects/dd8-data-hml/locations/us-central1/jobs/run-demo-job:run \
	-H "Authorization: Bearer ${ACCESS_TOKEN}" \
	-H "Content-Type: application/json" \
	-d @data.json
