package com.employee.employee_demo;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class EmployeServiceImpl implements EmployeeService {

	@Autowired
	private EmployeeRepository employeeRepository;

	@Override
	public void createEmployee(Employee employee) {
		employeeRepository.save(employee);

	}

	@Override
	public Employee getEmployee(int id) {

		return employeeRepository.findById(id);

	}

	@Override
	public Employee updateEmployee(Employee employee) {
		return employeeRepository.save(employee);
	}

	@Override
	public void deleteEmployee(int id) {
		employeeRepository.delete(id);

	}

	@Override
	public List<Employee> getAllEmployees() {

		List<Employee> employee = new ArrayList<>();
		employeeRepository.findAll().forEach(employee::add);
		return employee;
	}

	/*
	 * public void run(int... args) throws Exception {
	 * 
	 * moreage(); }
	 * 
	 * private void moreage() { System.out.println("age"); List<Employee>
	 * employee = new ArrayList<>();
	 * employeeRepository.findEmployeeHasAgeGreaterThan(30);
	 * employee.forEach(System.out::println);
	 * 
	 * }
	 */
}
