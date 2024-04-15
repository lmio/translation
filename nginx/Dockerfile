FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY templates/ /etc/nginx/templates/
ENV NGINX_ENTRYPOINT_LOCAL_RESOLVERS 1
ENV BACKEND_HOST app
ENV BACKEND_PORT 9000
