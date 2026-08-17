% rebase('layout-gui.tpl', apipath=apipath)

<div class="cont">
    <h1>PGP Key Management</h1>
    <h2>Add Key</h2>
    <div class="form-group">
        <form action="{{ apipath }}" method="POST">
            <input type="text" placeholder="name" id="name" />
            <input type="text" placeholder="key" id="key" />
            <button type="submit">Submit</button>
        </form>
    </div>
</div>
