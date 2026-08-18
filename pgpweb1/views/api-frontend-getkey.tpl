% rebase('api-frontend.tpl', apipath=apipath, title='Get Key')

<form action="{{ apipath }}" method="POST">
    <input type="text" placeholder="name" name="name" />
    <button type="submit">Submit</button>
</form>

