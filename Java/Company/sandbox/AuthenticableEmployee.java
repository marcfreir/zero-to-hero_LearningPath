//package com.company;

public abstract class AuthenticableEmployee extends Employee
{
    private int password;

    public boolean authenticate(int password)
    {
		return this.password == password;
	}
}