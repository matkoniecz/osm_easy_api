from typing import TYPE_CHECKING
if TYPE_CHECKING: # pragma: no cover
    from ...api import Api

from ...api import exceptions

class Changeset_Discussion_Container:
    def __init__(self, outer):
        self.outer: "Api" = outer

    def comment(self, changeset_id: int, text: str) -> None:
        """Add a comment to a changeset.

        Args:
            changeset_id (int): Changeset id.
            text (str): The comment text.

        Raises:
            exceptions.ChangesetNotClosed: Changeset must be closed to add comment.
        """
        response = self.outer._request(self.outer._RequestMethods.POST, self.outer._url.changeset_discussion["comment"].format(id=changeset_id, text=text), self.outer._Requirement.YES, auto_status_code_handling=False)
        
        match response.status_code:
            case 200: pass
            case 409: raise exceptions.ChangesetNotClosed()

    def subscribe(self, changeset_id: int) -> None:
        """Subscribe to the discussion to recive notifications for new comments.

        Args:
            changeset_id (int): Changeset id.

        Raises:
            exceptions.AlreadySubscribed: You are already subscribed to this changeset.
        """
        response = self.outer._request(self.outer._RequestMethods.POST, self.outer._url.changeset_discussion["subscribe"].format(id=changeset_id), self.outer._Requirement.YES, auto_status_code_handling=False)
        
        match response.status_code:
            case 200: pass
            case 409: raise exceptions.AlreadySubscribed()

    def unsubscribe(self, changeset_id: int) -> None:
        """Unsubscribe from discussion to stop reciving notifications.

        Args:
            changeset_id (int): Changeset id.

        Raises:
            exceptions.NotSubscribed: You are not subscribed to this changeset.
        """
        response = self.outer._request(self.outer._RequestMethods.POST, self.outer._url.changeset_discussion["unsubscribe"].format(id=changeset_id), self.outer._Requirement.YES, auto_status_code_handling=False)
        
        match response.status_code:
            case 200: pass
            case 404: raise exceptions.NotSubscribed()

    def hide(self, comment_id: int) -> None:
        """Set visible flag on changeset comment to false. MODERATOR ONLY!

        Args:
            comment_id (int): Comment id.

        Raises:
            exceptions.NotAModerator: You are not a moderator.
            exceptions.IdNotFoundError: Comment with provided id not found.
        """
        response = self.outer._request(self.outer._RequestMethods.POST, self.outer._url.changeset_discussion["hide"].format(comment_id=comment_id), self.outer._Requirement.YES, auto_status_code_handling=False)
        
        match response.status_code:
            case 200: pass
            case 403: raise exceptions.NotAModerator()
            case 404: raise exceptions.IdNotFoundError()

    def unhide(self, comment_id: int) -> None:
        """Set visible flag on changeset comment to true. MODERATOR ONLY!

        Args:
            comment_id (int): Comment id.

        Raises:
            exceptions.NotAModerator: You are not a moderator.
            exceptions.IdNotFoundError: Comment with provided id not found.
        """
        response = self.outer._request(self.outer._RequestMethods.POST, self.outer._url.changeset_discussion["unhide"].format(comment_id=comment_id), self.outer._Requirement.YES, auto_status_code_handling=False)
        
        match response.status_code:
            case 200: pass
            case 403: raise exceptions.NotAModerator()
            case 404: raise exceptions.IdNotFoundError()