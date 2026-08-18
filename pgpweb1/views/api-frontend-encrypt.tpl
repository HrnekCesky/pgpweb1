% rebase('api-frontend.tpl', apipath=apipath, title='Encrypt')

<form action="{{ apipath }}" method="POST">
    <input type="text" placeholder="key name" name="name" />
    <textarea placeholder="text to encrypt" name="text"></textarea>
    <button type="submit">Submit</button>
</form>
