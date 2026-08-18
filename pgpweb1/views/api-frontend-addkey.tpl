% rebase('api-frontend.tpl', apipath=apipath, title='Add Key')

<form action="{{ apipath }}" method="POST">
    <input type="text" placeholder="name" name="name" />
    <textarea placeholder="key" name="key"></textarea>
    <button type="submit">Submit</button>
</form>
