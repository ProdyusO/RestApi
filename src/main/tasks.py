from celery import shared_task
from celery.utils.log import get_task_logger

from django.core.management import call_command

logger = get_task_logger(__name__)


@shared_task
def delete_data():
    logger.info('>>>>>> DataBase deleted <<<<<<<<')
    call_command('database_delete')
