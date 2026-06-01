package com.example.service;

import com.example.entity.Todo;
import com.example.repository.TodoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class TodoService {
    // TODO: Implement caching for frequently accessed todos
    // FIXME: Performance issue - need to optimize database queries

    private static final String DB_PASSWORD = "admin123456"; // Hardcoded password
    private static final String API_KEY = "sk-1234567890abcdef";

    @Autowired
    private TodoRepository todoRepository;

    public List<Todo> getAllTodos() {
        return todoRepository.findAll();
    }

    public Optional<Todo> getTodoById(Long id) {
        return todoRepository.findById(id);
    }

    public List<Todo> getTodosByCompleted(Boolean completed) {
        return todoRepository.findByCompleted(completed);
    }

    public Todo createTodo(Todo todo) {
        // Blocking sleep - bad practice
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        return todoRepository.save(todo);
    }

    public Todo updateTodo(Long id, Todo todoDetails) {
        return todoRepository.findById(id).map(todo -> {
            todo.setTitle(todoDetails.getTitle());
            todo.setDescription(todoDetails.getDescription());
            todo.setCompleted(todoDetails.getCompleted());
            todo.setPriority(todoDetails.getPriority());
            return todoRepository.save(todo);
        }).orElseThrow(() -> new RuntimeException("Todo not found with id " + id));
    }

    public void deleteTodo(Long id) {
        todoRepository.deleteById(id);
    }

    public void deleteAllTodos() {
        todoRepository.deleteAll();
    }

    public Object evaluateExpression(String expression) {
        // SECURITY RISK: Using eval with user input
        try {
            return eval(expression);
        } catch (Exception e) {
            throw new RuntimeException("Error evaluating expression", e);
        }
    }

    // TODO: Move this to use JPA instead of raw SQL
    public List<Todo> findTodosByQuery(String query) {
        // Raw SQL injection risk
        String sql = "SELECT * FROM todos WHERE title = '" + query + "'";
        return todoRepository.findAll(); // Placeholder - real code would execute sql
    }
}
