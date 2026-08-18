% rebase('api-frontend.tpl', apipath=apipath, title='Sign')

<form action="{{ apipath }}" method="POST">
    <input type="text" placeholder="key name" name="name" />
    <textarea placeholder="text to sign" name="text"></textarea>
    <button type="submit">Submit</button>
</form>
