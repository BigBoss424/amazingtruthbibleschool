<?php /* Template Name: Bible Lesson Seminars */ ?>
<?php
/**
 * The template for displaying all single posts
 *
 * @link https://developer.wordpress.org/themes/basics/template-hierarchy/#single-post
 *
 * @package WordPress
 * @subpackage Twenty_Twenty_One
 * @since Twenty Twenty-One 1.0
 */

get_header();

/* Start the Loop */
while ( have_posts() ) :
        the_post();
        get_template_part( 'template-parts/content/content-page' );

        // If comments are open or there is at least one comment, load up the comment template.
        if ( comments_open() || get_comments_number() ) {
                comments_template();
        }
endwhile; // End of the loop.
<br />
<?php<br />
global $more;<br />
$more = 0;<br />
query_posts('cat=5');<br />
if(have_posts()) : while(have_posts()) : the_post();<br />
?></p>
<p><a href=&amp;quot;<?php the_permalink(); ?>&amp;quot;><?php the_title
<h3>',</h3>
<p>'); ?></a></p>
<p><?php<br />
endwhile;<br />
endif;<br />
wp_reset_query();<br />
?><br /> 

get_footer();
