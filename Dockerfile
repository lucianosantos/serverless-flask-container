FROM public.ecr.aws/lambda/python:3.11
COPY . ${LAMBDA_TASK_ROOT}
COPY requirements.txt  .
RUN  pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

CMD ["app.handler"]