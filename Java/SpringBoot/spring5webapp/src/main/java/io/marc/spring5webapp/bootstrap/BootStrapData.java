package io.marc.spring5webapp.bootstrap;

import io.marc.spring5webapp.domain.Author;
import io.marc.spring5webapp.domain.Book;
import io.marc.spring5webapp.repositories.AuthorRepository;
import io.marc.spring5webapp.repositories.BookRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class BootStrapData implements CommandLineRunner {

    private final AuthorRepository authorRepository;
    private final BookRepository bookRepository;

    public BootStrapData(AuthorRepository authorRepository, BookRepository bookRepository) {
        this.authorRepository = authorRepository;
        this.bookRepository = bookRepository;
    }

    @Override
    public void run(String... args) throws Exception {

        Author marc = new Author("Marc", "Freir");
        Book javaFNH = new Book("Java For Non-humans", "1234567");
        marc.getBooks().add(javaFNH);
        javaFNH.getAuthors().add(marc);

        authorRepository.save(marc);
        bookRepository.save(javaFNH);

        Author timmy = new Author("Timmy", "Lee");
        Book programmingFF = new Book("Programming For Fun", "7894561");
        timmy.getBooks().add(programmingFF);
        programmingFF.getAuthors().add(timmy);

        authorRepository.save(timmy);
        bookRepository.save(programmingFF);

        System.out.println("Started in Bootstrap");
        System.out.println("Number of Books: " + bookRepository.count());
    }
}
