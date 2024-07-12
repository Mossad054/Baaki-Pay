from flask import render_template, redirect, url_for, flash
from models import db, Customer, Merchant
from forms import CustomerRegistrationForm, MerchantRegistrationForm

def register_customer():
    form = CustomerRegistrationForm()
    if form.validate_on_submit():
        customer = Customer(username=form.username.data,
                            email=form.email.data,
                            address=form.address.data)
        customer.set_password(form.password.data)
        db.session.add(customer)
        db.session.commit()
        flash('Congratulations, you are now a registered customer!')
        return redirect(url_for('index'))
    return render_template('register_customer.html', title='Register Customer', form=form)

def register_merchant():
    form = MerchantRegistrationForm()
    if form.validate_on_submit():
        merchant = Merchant(username=form.username.data,
                            email=form.email.data,
                            business_name=form.business_name.data,
                            business_address=form.business_address.data)
        merchant.set_password(form.password.data)
        db.session.add(merchant)
        db.session.commit()
        flash('Congratulations, you are now a registered merchant!')
        return redirect(url_for('index'))
    return render_template('register_merchant.html', title='Register Merchant', form=form)
