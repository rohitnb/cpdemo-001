## Demo Checklist

- [ ] Install Copilot extension
- [ ] Create a new branch for currency conversion
- [ ] Add the new functions in `calcfunctions.py` with Copilot's help - `getExchangeRate` and `currencyConvert`
- [ ] Add a new landing page say `cconv.html`. Use Copilot to play with some drop down options for `source`. Show that it picks up for `target` as well. Make it add the `amount` and `submit` buttons 
- [ ] Add a new results page - `cconvresults.html`
- [ ] `app.py` new routes
    - [ ] `cconv` - Render the cconv.html
    - [ ] `cconvresults` - Use `POST` and pass the inputs `source`, `target`, `amount` 
- [ ] Write new tests in `calcfunctions-test.py`
- [ ] Test using `pytest calcfunctions-test.py`
