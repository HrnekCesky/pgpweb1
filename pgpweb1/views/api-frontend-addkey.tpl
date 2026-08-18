% rebase('layout-gui.tpl', apipath=apipath, title='Add Key')

<div class="cont">
    <h1>PGP Key Management</h1>
    <h2>Add Key</h2>
    <div class="form-group">
        <form action="{{ apipath }}" method="POST">
            <input type="text" placeholder="name" name="name" />
            <textarea placeholder="key" name="key"></textarea>
            <button type="submit">Submit</button>
        </form>
    </div>
</div>
