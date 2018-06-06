# MAINTAINER Jonathan Mainguy <jon@soh.re>
FROM centos:latest
LABEL version=0.1-1
RUN yum install -y https://pulp.soh.re/pulp/repos/sohre/el7/Packages/h/http_whois-0.1-1.el7.centos.x86_64.rpm whois
USER http_whois
EXPOSE 8080
CMD ["/usr/sbin/http_whois"]
