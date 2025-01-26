document.addEventListener('DOMContentLoaded', function() {
    // Like button functionality (Example)
    const likeButton = document.querySelectorAll('.like-button');
    likeButton.forEach(button => {
        button.addEventListener('click', function() {
            let likeCount = parseInt(button.nextElementSibling.textContent);
            likeCount++;
            button.nextElementSibling.textContent = likeCount;
        });
    });

    // Submit a comment (example of basic comment functionality)
    const commentForm = document.getElementById('commentForm');
    if (commentForm) {
        commentForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const commentText = document.getElementById('newComment').value;
            const commentList = document.getElementById('commentList');
            if (commentText) {
                const newComment = document.createElement('li');
                newComment.textContent = commentText;
                commentList.appendChild(newComment);
                document.getElementById('newComment').value = ''; // Clear the input
            }
        });
    }
});
