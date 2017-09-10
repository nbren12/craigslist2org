Generate org-mode entries from a craigslist url

To install, call

    pip install git+https://github.com/nbren12/craigslist2org

and add the following to your .emacs file:

```elisp
(defun craigslist-org ()
  ;; pull info from craigslist page into org-mode header
  (interactive)
  (let ((url (read-string "Enter Craigslist URL: ")))
    (org-insert-heading-respect-content)
    (insert
    (shell-command-to-string (concat "craigslist2org.py -n 0 " url)))))

(evil-leader/set-key "oc" 'craigslist-org)
```
