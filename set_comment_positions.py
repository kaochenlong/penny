import positions.fields
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    from django import setup
    setup()

    from comments.models import Comment
    from nannies.models import Nanny

    def set_comment_positions():
      for nanny in Nanny.objects.all():
          comments = Comment.objects.filter(nanny=nanny).order_by('id')
          position = 0
          for comment in comments:
              comment.position = position
              comment.save()
              position += 1

    set_comment_positions()
