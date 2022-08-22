#!/bin/sh
if [ -z "${BOKEH_PREFIX}" ]; then
    PREFIX_PARAM="";
else
    PREFIX_PARAM="--prefix ${BOKEH_PREFIX}";
fi
echo "Launching Airflow webserver"
airflow webserver &
echo "Launching Airflow scheduler"
airflow scheduler &
echo "Launching Bokeh Server..."
bokeh serve --port ${BOKEH_PORT} --address 0.0.0.0 --allow-websocket-origin "*" ${PREFIX_PARAM} --log-level ${BOKEH_LOG_LEVEL} ~/kafka_stock/pipeline