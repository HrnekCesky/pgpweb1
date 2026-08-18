% rebase('layout-gui.tpl', apipath=apipath, title='Get Key')

<div class="cont">
    <h1>PGP Key Management</h1>
    <h2>Get Key</h2>
    <div class="form-group">
        <form action="{{ apipath }}" method="POST">
            <input type="text" placeholder="name" name="name" />
            <button type="submit">Submit</button>
        </form>
    </div>
</div>
