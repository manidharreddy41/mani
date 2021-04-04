package com.employee.employee_demo;

import org.springframework.data.cassandra.mapping.Column;
import org.springframework.data.cassandra.mapping.PrimaryKey;
import org.springframework.data.cassandra.mapping.Table;

@Table("employee")
public class Employee {

	public Employee() {
		super();
		// TODO Auto-generated constructor stub
	}

	@PrimaryKey("id")
	private int id;

	@Column("name")
	private String name;

	@Column
	private int age;

	@Column("salary")
	private float salary;

	@Column("info")
	private String info;

	public String getinfo() {
		return info;

	}

	public void setinfo(String info) {
		this.info = info;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public float getSalary() {
		return salary;
	}

	public void setSalary(float salary) {
		this.salary = salary;
	}

}
