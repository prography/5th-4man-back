#! /usr/bin/env bash
git add -f secrets.json
eb deploy --profile fourman --staged
git reset HEAD secrets.json