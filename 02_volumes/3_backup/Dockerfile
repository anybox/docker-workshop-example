FROM alpine

COPY backup.sh /usr/src/app/backup.sh

VOLUME /backup
ENTRYPOINT ["sh", "/usr/src/app/backup.sh"]
CMD "-h"