## Pre-requisites

- You must have VS Code installed for this to work:
- You must have Python installes and an environment variable set on your PATH corresponding to `python`

## To set up a Powershell Profile

### Steps

- Run `code $PROFILE`

## To set up an environment variable

### Steps

Add the following code:

```
function Move-Obsidian-Pics {
    & 'python' 'D:\Github\Python\Obsidian-Image-Mover\move-obsidian-images.py'
}

Set-Alias -Name MoveObsidianPics -Value Move-Obsidian-Pics
```
