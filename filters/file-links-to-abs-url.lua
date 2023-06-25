-- While following code file links in Org mode (C-c C-o), viewing Emacs Org-mode
-- backend converted html in browser (via C-c C-e h o), or viewing the locally
-- built html by pandoc, the hyperlinks to code files are of `file:` scheme. 
-- While building the html to be deployed to Github Pages, use this Pandoc Lua 
-- filter to replace file linlks to absolute URLs.
-- TODO: elem.target does not include the url scheme. Include the source files
-- in github-pages artifact for now.
return {{
    Link = function(elem)
        if elem.target:match("^file:") then
            elem.target = elem.target:gsub("^file:", "https://github.com/Roytangrb/dsa/blob/master/")
        end
        return elem
    end
}}

